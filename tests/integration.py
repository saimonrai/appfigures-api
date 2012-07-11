import json
import unittest

from appfigures import api, sales, events
from appfigures.services import ResultService
from appfigures.transport import HttpResponse
from datetime import date
from mock import MagicMock


class LocalIntegrationTest(unittest.TestCase):


    def setUp(self):
        self.requester = MagicMock()
        result_service = create_closed_result_service(self.requester, api.PODIO_API_URL_1_1)
        self.client = api.Client("test", "test", result_service=result_service)
        
        self.startdate = date(2012, 1, 1)
        self.enddate = date(2012, 2, 2)
        self.products = [10000, 20000, 30000]
        self.event_id = 111111
        self.caption = "Test Caption"
        self.usa = "US"
        self.response = MagicMock()
        self.response.text = '{ "Success": true }'
        self.response.status_code = 200
        self.return_response = HttpResponse(self.response)
        self.return_dict = { "Success": True }

    #GET
    def test_get_sales_report_by_product(self):
        
        self.requester.get.return_value = self.return_response
        
        report = self.client.get_sales_report_by_product(self.startdate, self.enddate, 
                                                         data_source=api.DATASOURCE_DAILY, 
                                                         products=self.products, country=self.usa)
        
        expected_url = "{0}/{1}/{2}/{3}/{4}".format(api.PODIO_API_URL_1_1, 
                                                    sales.SALES_BASE_URI, 
                                                    sales.SALES_BY_PRODUCT, 
                                                    self.startdate.isoformat(), 
                                                    self.enddate.isoformat())
        
        expected_params = { 
            "dataSource": api.DATASOURCE_DAILY, 
            "products": ';'.join(str(i) for i in self.products),
            "country": self.usa
        }
        
        self.assertDictEqual(report, self.return_dict)
        self.requester.get.assert_called_once_with(expected_url, expected_params)
    
    #POST   
    def test_create_new_event(self):
        self.requester.post.return_value = self.return_response
        
        event = self.client.create_new_event(self.caption, self.startdate, self.products)
        
        expected_url = "{0}/{1}".format(api.PODIO_API_URL_1_1, events.EVENTS_BASE_URI)
        expected_params = json.dumps({
            "caption": self.caption,
            "date": self.startdate.isoformat(),
            "products": self.products
        })
        
        self.assertDictEqual(event, self.return_dict)
        self.requester.post.assert_called_once_with(expected_url, expected_params)
    
    #PUT
    def test_update_event(self):
        self.requester.put.return_value = self.return_response
        
        event = self.client.update_event(self.event_id, self.caption, 
                                         self.startdate, self.products)
        
        expected_url = "{0}/{1}/{2}".format(api.PODIO_API_URL_1_1, 
                                            events.EVENTS_BASE_URI, 
                                            self.event_id)
        expected_body = json.dumps({
            "caption": self.caption,
            "date": self.startdate.isoformat(),
            "products": self.products
        })
        
        self.assertDictEqual(event, self.return_dict)
        self.requester.put.assert_called_once_with(expected_url, expected_body)
    
    #DELETE
    def test_delete_event(self):
        self.requester.delete.return_value = self.return_response
        
        result = self.client.delete_event(self.event_id)
        
        expected_url = "{0}/{1}/{2}".format(api.PODIO_API_URL_1_1, 
                                            events.EVENTS_BASE_URI, 
                                            self.event_id)
        
        self.assertDictEqual(result, self.return_dict)
        self.requester.delete.assert_called_once_with(expected_url)
        

def create_closed_result_service(requester, base_url):
    from appfigures.serialization import JsonSerializer
    from appfigures.urls import AppFiguresUrlBuilder
    
    serializer = JsonSerializer()
    url_builder = AppFiguresUrlBuilder(base_url)
    
    return ResultService(requester, serializer, url_builder)
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
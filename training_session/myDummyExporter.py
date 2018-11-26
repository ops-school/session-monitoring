#!/usr/bin/env python3
import socket
import random
rand=random.Random()

# setup global_variable
my_dict={}
my_dict['DummyService_requests{caller="APT",}']= 10008.0
my_dict['DummyService_errors{}']= 43.0
my_dict['DummyService_duration_summary{quantile="0.5",}']= 0.0
my_dict['DummyService_duration_summary{quantile="0.75",}']= 0.0
my_dict['DummyService_duration_summary{quantile="0.95",}']= 0.0
my_dict['DummyService_duration_summary{quantile="0.98",}']= 0.0
my_dict['DummyService_duration_summary{quantile="0.99",}']= 0.0
my_dict['DummyService_duration_summary{quantile="0.999",}']= 0.0
my_dict['DummyService_duration_summary_count{}']= 10008.0
my_dict['DummyService_duration_summary_sum{}']= 433354.0
my_dict['DummyService_duration_cumulative_bucket{le="10.0",}']= 5056.0
my_dict['DummyService_duration_cumulative_bucket{le="20.0",}']= 5702.0
my_dict['DummyService_duration_cumulative_bucket{le="30.0",}']= 6333.0
my_dict['DummyService_duration_cumulative_bucket{le="40.0",}']= 6963.0
my_dict['DummyService_duration_cumulative_bucket{le="50.0",}']= 7592.0
my_dict['DummyService_duration_cumulative_bucket{le="60.0",}']= 8005.0
my_dict['DummyService_duration_cumulative_bucket{le="70.0",}']= 8381.0
my_dict['DummyService_duration_cumulative_bucket{le="80.0",}']= 8774.0
my_dict['DummyService_duration_cumulative_bucket{le="90.0",}']= 9178.0
my_dict['DummyService_duration_cumulative_bucket{le="+Inf",}']= 10008.0
my_dict['DummyService_duration_non_cumulative_bucket{le="10.0",}']= 5056.0
my_dict['DummyService_duration_non_cumulative_bucket{le="20.0",}']= 646.0
my_dict['DummyService_duration_non_cumulative_bucket{le="30.0",}']= 631.0
my_dict['DummyService_duration_non_cumulative_bucket{le="40.0",}']= 630.0
my_dict['DummyService_duration_non_cumulative_bucket{le="50.0",}']= 629.0
my_dict['DummyService_duration_non_cumulative_bucket{le="60.0",}']= 413.0
my_dict['DummyService_duration_non_cumulative_bucket{le="70.0",}']= 377.0
my_dict['DummyService_duration_non_cumulative_bucket{le="80.0",}']= 392.0
my_dict['DummyService_duration_non_cumulative_bucket{le="90.0",}']= 404.0
my_dict['DummyService_duration_non_cumulative_bucket{le="+Inf",}']= 830.0



def update_dict():
  my_dict['DummyService_requests{caller="APT",}']+=rand.randint(0, 100)
  my_dict['DummyService_errors{}']+=rand.randint(0, 10)
  my_dict['DummyService_duration_summary_count{}']+=rand.randint(0, 100)
  my_dict['DummyService_duration_summary_sum{}']+=rand.randint(0, 1000)
  my_dict['DummyService_duration_summary{quantile="0.5",}']+=+rand.randint(0, 10)
  my_dict['DummyService_duration_summary{quantile="0.75",}']=(my_dict['DummyService_duration_summary{quantile="0.75",}']+rand.randint(0, 10))
  my_dict['DummyService_duration_summary{quantile="0.95",}']=(my_dict['DummyService_duration_summary{quantile="0.75",}']+rand.randint(0, 10))
  my_dict['DummyService_duration_summary{quantile="0.98",}']=(my_dict['DummyService_duration_summary{quantile="0.95",}']+rand.randint(0, 10))
  my_dict['DummyService_duration_summary{quantile="0.99",}']=(my_dict['DummyService_duration_summary{quantile="0.99",}']+rand.randint(0, 10))
  my_dict['DummyService_duration_summary{quantile="0.999",}']=(my_dict['DummyService_duration_summary{quantile="0.999",}']+rand.randint(0, 10))
  #OK
  my_dict['DummyService_duration_non_cumulative_bucket{le="10.0",}']+=(5-rand.randint(0, 10))
  my_dict['DummyService_duration_non_cumulative_bucket{le="20.0",}']+=(5-rand.randint(0, 10))
  my_dict['DummyService_duration_non_cumulative_bucket{le="30.0",}']+=(5-rand.randint(0, 10))
  my_dict['DummyService_duration_non_cumulative_bucket{le="40.0",}']+=(5-rand.randint(0, 10))
  my_dict['DummyService_duration_non_cumulative_bucket{le="50.0",}']+=(5-rand.randint(0, 10))
  my_dict['DummyService_duration_non_cumulative_bucket{le="60.0",}']+=(5-rand.randint(0, 10))
  my_dict['DummyService_duration_non_cumulative_bucket{le="70.0",}']+=(5-rand.randint(0, 10))
  my_dict['DummyService_duration_non_cumulative_bucket{le="80.0",}']+=(5-rand.randint(0, 10))
  my_dict['DummyService_duration_non_cumulative_bucket{le="90.0",}']+=(5-rand.randint(0, 10))
  my_dict['DummyService_duration_non_cumulative_bucket{le="+Inf",}']+=(5-rand.randint(0, 10))
  #OK
  my_dict['DummyService_duration_cumulauration_cumulative_bucket{le="10.0",}']=my_dict['DummyService_duration_non_cumulative_bucket{le="10.0",}']
  my_dict['DummyService_dtive_bucket{le="20.0",}']=my_dict['DummyService_duration_cumulative_bucket{le="10.0",}']+my_dict['DummyService_duration_non_cumulative_bucket{le="20.0",}']
  my_dict['DummyService_duration_cumulative_bucket{le="30.0",}']=my_dict['DummyService_duration_cumulative_bucket{le="20.0",}']+my_dict['DummyService_duration_non_cumulative_bucket{le="30.0",}']
  my_dict['DummyService_duration_cumulative_bucket{le="40.0",}']=my_dict['DummyService_duration_cumulative_bucket{le="30.0",}']+my_dict['DummyService_duration_non_cumulative_bucket{le="40.0",}']
  my_dict['DummyService_duration_cumulative_bucket{le="50.0",}']=my_dict['DummyService_duration_cumulative_bucket{le="40.0",}']+my_dict['DummyService_duration_non_cumulative_bucket{le="50.0",}']
  my_dict['DummyService_duration_cumulative_bucket{le="60.0",}']=my_dict['DummyService_duration_cumulative_bucket{le="50.0",}']+my_dict['DummyService_duration_non_cumulative_bucket{le="60.0",}']
  my_dict['DummyService_duration_cumulative_bucket{le="70.0",}']=my_dict['DummyService_duration_cumulative_bucket{le="60.0",}']+my_dict['DummyService_duration_non_cumulative_bucket{le="70.0",}']
  my_dict['DummyService_duration_cumulative_bucket{le="80.0",}']=my_dict['DummyService_duration_cumulative_bucket{le="70.0",}']+my_dict['DummyService_duration_non_cumulative_bucket{le="80.0",}']
  my_dict['DummyService_duration_cumulative_bucket{le="90.0",}']=my_dict['DummyService_duration_cumulative_bucket{le="80.0",}']+my_dict['DummyService_duration_non_cumulative_bucket{le="90.0",}']
  my_dict['DummyService_duration_cumulative_bucket{le="+Inf",}']=my_dict['DummyService_duration_cumulative_bucket{le="90.0",}']+my_dict['DummyService_duration_non_cumulative_bucket{le="+Inf",}']

def create_data():
   update_dict()
   return_string=''
   for key in my_dict:
    return_string+=key+' '+str(my_dict[key])+"\n"
   return return_string

#HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 65433        # Port to listen on (non-privileged ports are > 1023)
try:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind((HOST, PORT))
      s.listen()
      while True:
         conn, addr = s.accept()
         with conn:
             while True:
                 data = conn.recv(1024)
                 if not data:
                     break
                 return_data=create_data()
                 conn.sendall(bytes(return_data, 'utf-8'))
                 break
except()  as e:
  s.close()

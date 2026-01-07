# FastApiLimiter

## Description

Faced with problem - my program that used FastAPI worked perfectly but sometimes could give error due to a lot of requests

I haven't found an open-source solution in the internet so decided to create my own.

There are two ways of limiting requests based on your needs:
  1. Limit concurrent requests per second. It will
      Example: Limit 10, Sent 11 requests (that take about 0.5 second to complete) in 20:22:11. Regularly It will process all 11 requests together and it will end at 20:22:11.5 but with my solution it will take approximately 1.5s - will end at 20:22:12.5
         
  2. Set limit on maximum concurrent requests.
     Example: Limit 10, Sent 11 requests - It will make 10 requests concurrently and when the first will be finished it will start the last request


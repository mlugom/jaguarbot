import http.server
import os
import rospkg

PORT = 5000

r = rospkg.RosPack()
path = r.get_path('jaguarbot')

os.chdir(f'{path}/web')

server_object = http.server.HTTPServer(('',PORT),http.server.CGIHTTPRequestHandler)

print(f'App hosted at port {PORT}')
server_object.serve_forever()
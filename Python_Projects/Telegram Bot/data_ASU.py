from const_file import *

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))


token = "6387194055:AAHiHtmkG7VQLePOKQ7FCvOb4D6xQiP2npg"
url = "djttcote2.pythonanywhere.com/"
main_poll_id = 20186
main_poll_id_num = "5886602130592104649"
rm_approve_fun = True
rm_alarm_msg = True

def save_update(id, string):
    pass
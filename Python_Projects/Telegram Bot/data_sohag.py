from const_file import *

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))


token = "6330074336:AAGMMabZRDwm7wg1SEEs4JZUeRNep0Juz94"
url = "djttcote.pythonanywhere.com/"
main_poll_id = 20095
main_poll_id_num = "5866116996311023836"
privacy_msg_id = 20094
rm_approve_fun = False
rm_alarm_msg = False
def save_update(id, string):
    pass
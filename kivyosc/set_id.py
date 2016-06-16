
class id_setter:
    def __init__(self):
        id_setting_file = open('/boot/set_id', 'r')
        ip_config_file = open('/home/pi/KivyPi/config/ip_conf_sample', 'r')
        self.id_to_set = id_setting_file.read().strip()
        self.ip_config_= ip_config_file.read()

    def set_to_new_ip(self):
        if 1 <= self.id_to_set <= 9:
            new_ip_config = self.ip_config.replace('replace_id_here', '23'+self.id_to_set)
            ip_set_file = open('/etc/dhcpcd.conf', 'w')
            ip_set_file.write(new_ip_config)
            ip_set_file.close()
        else:
            print('The ID not a valid number')

        print('ID Set Done')




id_file = open('/boot/set_id', 'r')
id_to_set = id_file.read().strip()
print('id to set: %s' % id_to_set)
id_file.close()

ip_config_file = open('/home/pi/SyncPi8/ip_conf_sample', 'r')
ip_config = ip_config_file.read()
ip_config_file.close()


if 200 < int(id_to_set) < 255:
    new_ip_config = ip_config.replace('replace_id_here', id_to_set)
    ip_set_file = open('/etc/dhcpcd.conf', 'w')
    ip_set_file.write(new_ip_config)
    print("new config: %s" % new_ip_config)
    ip_set_file.close()
else:
    print('id not a valid number')

print('script done')
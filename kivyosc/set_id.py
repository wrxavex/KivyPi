
class id_setter:
    def __init__(self):
        id_setting_file = open('/boot/set_id', 'r')
        ip_config_file = open('/home/pi/KivyPi/config/ip_conf_sample', 'r')
        self.locked = 0
        self.id_to_set = id_setting_file.read().strip()
        self.ip_config = ip_config_file.read()
        self.my_movie = "/home/pi/newTaipei/"+self.id_to_set+".mp4"

    def set_to_new_ip(self):
        id_int = int(self.id_to_set)
        if 1 <= id_int <= 9:
            new_ip_config = self.ip_config.replace('replace_id_here', '23'+str(id_int))
            ip_set_file = open('/etc/dhcpcd.conf', 'w')
            ip_set_file.write(new_ip_config)
            ip_set_file.close()
        else:
            print('The ID not a valid number')

        print('ID Set Done')
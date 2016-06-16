
class id_setter:
    def __init__(self):
        id_setting_file = open('/boot/set_id', 'r')
        ip_config_file = open('/home/pi/KivyPi/config/ip_conf_sample', 'r')
        self.locked = 0
        self.id_to_set = id_setting_file.read().strip()
        self.ip_config_= ip_config_file.read()
        self.my_movie = "/home/pi/newTaipei/"+self.id_to_set+".mp4"

    def set_to_new_ip(self):
        if 1 <= self.id_to_set <= 9:
            new_ip_config = self.ip_config.replace('replace_id_here', '23'+self.id_to_set)
            ip_set_file = open('/etc/dhcpcd.conf', 'w')
            ip_set_file.write(new_ip_config)
            ip_set_file.close()
        else:
            print('The ID not a valid number')

        print('ID Set Done')
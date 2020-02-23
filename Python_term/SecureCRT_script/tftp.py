# $language = "python"
# $interface = "1.0"
tftp_server_ip = "10.81.139.2"

def tftp_func(file_name):
    crt.Screen.WaitForString("fh-linux#")
    crt.Screen.Send("tftp -g -r {0} {1}".format(file_name, tftp_server_ip) + chr(13))

def Main():
    crt.Screen.Synchronous = True
    crt.Screen.Send(chr(13))
    tftp_func("test.sh")

    crt.Screen.Send("chmod +x test.sh" + chr(13))


Main()

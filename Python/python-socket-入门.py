-------------------------
socket-socket			 |
-------------------------
	* 网络七层模型
		物理层(线缆)
		数据链路层(mac)
		网络层(ip)
		传输层(udp/tcp)
		会话层
		表示层
		应用层

	* 常见的应用层网络协议
		http
		smtp
		dns
		ftp
		ssh
		snmp
		icmp
		dhcp
	
	* 学习地址

	
	* Python3中相关类库
		socket
			* 底层的 tcp/udp 类库
		socketserver
			* 对 socket 的封装
		
------------------------
python-socket-拆包/粘包	|
------------------------
	1,一端先发送数据大小到另一端
	2,另一端接收到数据大小后,保存,然后响应另一端,表示已经收到要接收的数据大小
	
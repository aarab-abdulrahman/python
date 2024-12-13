import socket

# إنشاء سوكت
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# الاتصال بالخادم (مثلاً الخادم على نفس الجهاز و المنفذ 12345)
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# استقبال الرسائل من الخادم
data = client_socket.recv(1024)  # 1024 هو الحجم الأقصى للبيانات التي نستقبلها
print("Received message from server:", data.decode())

# إغلاق الاتصال
client_socket.close()

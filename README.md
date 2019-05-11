# Config-HASSIO
Bản tổng hợp config Hassio
1. Flash hass vào thẻ
2. Đưa thẻ nhớ đã flash vào hass, cắm dây lan rồi cấp nguồn
3. Chờ khoảng 20 phút
4. Vào modelm hoặc router tìm ip của hass, cố định ip với mac luôn;
nếu dùng router thì vào modelm, vào mục DMZ khai báo ip của router, kích vào enable rồi save lại.
5. Vào router khai báo các cổng (mục "port forwating"), rồi khai báo các cổng 8123, 3218, 8321, 1883 về ip của pi
6. Đăng nhập vào hass: http://ip_pi:8123
7. Cài addon SSH, configuration hoặc ide, hoặc samba share. (Nếu dùng SSH thì có thể dùng winSCP để đăng nhập vào là tốt nhất)
8. Copy toàn bộ các file trong thư mục config vào trong thu mục tương ứng của hass, khai báo các thông số cần thiết.
9. Lưu lại, check config và reset hass
10. Sau khi reset nếu đã cài Duckdns thì đã bật ssl nên phải dùng: https://p_pi:8123


sdsd
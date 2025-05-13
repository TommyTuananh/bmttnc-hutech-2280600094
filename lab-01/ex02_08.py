 # Hàm kiểm tra số nhị phân chia hết cho 5 không
def chia_het_cho_5 (so_nhi_phan):
    #kiem tra xem soos thaapj pha chia het cho 5 khong
    so_thap_phan = int (so_nhi_phan, 2)
    if (so_thap_phan % 5 == 0):
        return True
    else:
        return False
# nhập chuỗi số nhị phân từ ng dùng chuoi
chuoi_so_nhi_phan = input ("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ")
#tách chuỗi thành các số nhị phân và kiểm tra số chia hết cho 5
so_nhi_phan_List = chuoi_so_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phan_List if chia_het_cho_5 (so)]
# in ra các số nhị phân chia hết cho 5
if len(so_chia_het_cho_5) > 0:
    ket_qua = ',' .join(so_chia_het_cho_5)
    print("Các số nhị phân chia hết cho 5 là: ", ket_qua)
else:
    print("Không có số nhị phân nào chia hết cho 5 trong chuỗi đã nhập. ")

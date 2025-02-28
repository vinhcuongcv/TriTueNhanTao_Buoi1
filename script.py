import temp


if __name__ == '__main__':
    while True:
        print("\nChọn bài tập để chạy:")
        print("1 - In tất cả các ký tự trong chuỗi 'your name'")
        print("2 - In tất cả các số lẻ từ 1 đến 10")
        print("3a - Tính tổng tất cả các số lẻ từ 1 đến 10")
        print("3b - Tính tổng tất cả các số từ 1 đến 6")
        print("4 - Các thao tác với từ điển (lấy khóa, giá trị, cặp khóa-giá trị)")
        print("5 - In danh sách các cặp (tên khóa học, tên khóa)")
        print("6 - Đếm số phụ âm trong chuỗi 'jabbawocky' (bằng hai cách)")
        print("7 - Chia 10 cho a với xử lý ngoại lệ (-2 ≤ a < 3)")
        print("8 - Sắp xếp danh sách các cặp (tuổi, tên) theo thứ tự tăng dần của tuổi")
        print("9 - Thao tác với tệp (mở tệp, đọc từng dòng, đọc toàn bộ)")
        print("10 - Tính tổng hai số")
        print("11 - Tạo ma trận 3x3 và vector, kiểm tra rank & shape")
        print("12 - Tạo ma trận mới từ M bằng phép toán (M + 3)")
        print("13 - Tính chuyển vị của ma trận M và vector v")
        print("14 - Tính chuẩn (norm) và chuẩn hóa vector x = (2,7)")
        print("15 - Thực hiện các phép toán vector a + b, a - b, a - c")
        print("16 - Tính tích vô hướng (dot product) của vector a và b")
        print("17 - Thao tác trên ma trận A (kiểm tra rank, shape, truy xuất phần tử)")
        print("18 - Tạo ma trận ngẫu nhiên 3x3 với giá trị trong khoảng (-10,10)")
        print("19 - Tạo ma trận đơn vị (identity matrix) 3x3")
        print("20 - Tính trace của một ma trận 3x3 (bằng hai cách)")
        print("21 - Tạo ma trận đường chéo 3x3 với các giá trị trên đường chéo là (1,2,3)")
        print("22 - Tính định thức (determinant) của ma trận A")
        print("23 - Tạo ma trận M từ hai vector cột a1 và a2")
        print("24 - Vẽ đồ thị y² với y trong khoảng (-5 đến 6)")
        print("25 - Tạo 4 giá trị cách đều nhau trong khoảng từ 0 đến 32")
        print("26 - Vẽ đồ thị y = x² với x trong khoảng (-5 đến 5)")
        print("27 - Vẽ đồ thị y = e^x với tiêu đề và nhãn trục")
        print("28 - Vẽ đồ thị y = log(x) với x từ 0 đến 5")
        print("29 - Vẽ hai đồ thị y = exp(x) và y = exp(2x) trên cùng một biểu đồ")
        print("30 - Vẽ hai đồ thị y = log(x) và y = log(2x) trên cùng một subplot")

        print("0 - Thoát chương trình")

        choice = input("Nhập số bài tập bạn muốn chạy: ")

        if choice == "1":
            name = input("Nhập tên của bạn: ")
            temp.Print_Name(name)
        elif choice == "2":
            temp.Print_All_Odd_Numbers()
        elif choice == "3a":
            temp.Sum_Odd_Numbers()
        elif choice == "3b":
            temp.Sum_From_1_To_6()
        elif choice == "4":
            temp.Dictionary_Operations()
        elif choice == "5":
            temp.print_course_name_pairs()
        elif choice == "6":
            temp.count_consonants()
        elif choice == "7":
            temp.divide_by_a()
        elif choice == "8":
            temp.sort_by_age()
        elif choice == "9":
            temp.file_operations()
        elif choice == "10":
            a = int(input("Nhap a : "))
            b = int(input("Nhap b : "))
            print(f"Sum = {temp.sum_two_numbers(a,b)}")
        elif choice == "11":
            temp.create_matrix_and_vector()
        elif choice == "12":
            temp.create_modified_matrix()
        elif choice == "13":
            temp.transpose_matrix_and_vector()
        elif choice == "14":
            temp.compute_norm_and_normalize()
        elif choice == "15":
            temp.vector_operations()
        elif choice == "16":
            temp.compute_dot_product()
        elif choice == "17":
            temp.matrix_operations()
        elif choice == "18":
            temp.create_random_matrix()
        elif choice == "19":
            temp.create_identity_matrix()
        elif choice == "20":
            temp.compute_trace()
        elif choice == "21":
            temp.create_diagonal_matrix()
        elif choice == "22":
            temp.compute_determinant()
        elif choice == "23":
            temp.create_matrix_M()
        elif choice == "24":
            temp.plot_square_y()
        elif choice == "25":
            temp.create_evenly_spaced()
        elif choice == "26":
            temp.plot_x_squared()
        elif choice == "27":
            temp.plot_exp()
        elif choice == "28":
            temp.plot_log()
        elif choice == "29":
            temp.plot_exp_functions()
        elif choice == "30":
            temp.plot_log_functions()
        elif choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")


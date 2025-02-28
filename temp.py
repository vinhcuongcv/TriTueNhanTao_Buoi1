import numpy as np
import matplotlib.pyplot as plt

# Phần 1 - Bài 1 : In tất cả các ký tự trong chuỗi 'your name'
def Print_Name(name):
    for char in name:
        print(char)
# Phần 1 - Bài 2 : In tất cả các số lẻ từ 1 đến 10
def Print_All_Odd_Numbers():
    for x in range(1, 11, 2):
        print(x)
# Phần 1 - Bài 3 :
def Sum_Odd_Numbers():
    print("Sum of odd numbers:", sum(range(1, 11, 2)))
# Phần 1 - Bài 4
def Sum_From_1_To_6():
    print("Sum from 1 to 6:", sum(range(1, 7)))
# Phần 1 - Bài 5
def Dictionary_Operations():
    mydict = {"a": 1, "b": 2, "c": 3, "d": 4}
    print("Keys:", list(mydict.keys()))
    print("Values:", list(mydict.values()))
    for key, value in mydict.items():
        print(f"{key}: {value}")
# Phần 1 - Bài 6

def print_course_name_pairs():
    courses = [131, 141, 142, 212]
    names = ["Maths", "Physics", "Chem", "Bio"]
    course_name_pairs = list(zip(courses, names))
    print(course_name_pairs)

# Phần 1 - Bài 7
def count_consonants():
    word = "jabbawocky"
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # Cách 1: Không dùng "continue"
    consonant_count_1 = sum(1 for char in word if char not in vowels)
    print("Consonant count (without continue):", consonant_count_1)

    # Cách 2: Dùng "continue"
    consonant_count_2 = 0
    for char in word:
        if char in vowels:
            continue
        consonant_count_2 += 1
    print("Consonant count (with continue):", consonant_count_2)

# Phần 1 - Bài 8
def divide_by_a():
    for a in range(-2, 3):
        try:
            result = 10 / a
            print(f"10 / {a} = {result}")
        except ZeroDivisionError:
            print(f"10 / {a} = can't divide by zero")
#Phần 1 - Bài 9
def sort_by_age():
    ages = [23, 10, 80]
    names = ["Hoa", "Lam", "Nam"]
    people = list(zip(ages, names))

    sorted_people = sorted(people, key=lambda x: x[0])
    print("Sorted by age:", sorted_people)

def file_operations():
    # a/ Mở file và đọc từng dòng
    print("\nĐọc file từng dòng:")
    with open("FirstName.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())

    # b/ Đọc toàn bộ nội dung file
    print("\nĐọc toàn bộ nội dung file:")
    with open("FirstName.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)

# Phần 2 - Bài 1
def sum_two_numbers(a, b):
    return a + b

#Phần 2 - Bài 2
def create_matrix_and_vector():
    # Tạo ma trận 3x3
    M = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    # Tạo vector hàng
    v = np.array([1, 2, 3])

    print("Matrix M:")
    print(M)

    print("\nVector v:")
    print(v)

    # Kiểm tra rank (hạng) của ma trận
    rank_M = np.linalg.matrix_rank(M)
    rank_v = np.linalg.matrix_rank(v.reshape(1, -1))  # Đưa v về dạng ma trận hàng để kiểm tra rank

    # Kiểm tra shape (kích thước)
    shape_M = M.shape
    shape_v = v.shape

    print("\nRank of matrix M:", rank_M)
    print("Shape of matrix M:", shape_M)
    print("\nRank of vector v:", rank_v)
    print("Shape of vector v:", shape_v)
# Phần 2 - Bài 3
def create_modified_matrix():
    M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    new_M = M + 3
    print("New Matrix (M + 3):\n", new_M)
# Phần 2 - Bài 4
def transpose_matrix_and_vector():
    M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    v = np.array([1, 2, 3])

    print("Transpose of M:\n", M.T)
    print("Transpose of v:\n", v.reshape(-1, 1))

# Phần 2 - Bài 5
def compute_norm_and_normalize():
    x = np.array([2, 7])
    norm_x = np.linalg.norm(x)
    normalized_x = x / norm_x if norm_x != 0 else x  # Tránh chia cho 0
    print(f"Norm of x: {norm_x}")
    print(f"Normalized x: {normalized_x}")

# Phần 2 - Bài 6
def vector_operations():
    a = np.array([10, 15])
    b = np.array([8, 2])
    c = np.array([1, 2, 3])

    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")

    try:
        print(f"a - c = {a - c}")  # Lỗi do khác kích thước
    except ValueError as e:
        print(f"Error: {e}")

#Phần 2 - Bài 7
def compute_dot_product():
    a = np.array([10, 15])
    b = np.array([8, 2])
    dot_product = np.dot(a, b)
    print(f"Dot product of a and b: {dot_product}")

#Phần 2 - Bài 8
def matrix_operations():
    A = np.array([[2, 4, 9], [3, 6, 7]])

    print(f"Rank of A: {np.linalg.matrix_rank(A)}")
    print(f"Shape of A: {A.shape}")
    print(f"Value at A[1,2] (7): {A[1,2]}")
    print(f"Second column of A:\n{A[:, 1]}")

#Phần 2 - Bài 9 : Tạo ma trận 3x3 trong phạm vi (-10;10)
def create_random_matrix():
    matrix = np.random.randint(-10, 11, (3,3))
    print(f"Random 3x3 matrix:\n{matrix}")

#Phần 2 - Bài 10 : Tạo ma trận đơn vị 3x3
def create_identity_matrix():
    matrix = np.eye(3)
    print(f"Identity 3x3 matrix:\n{matrix}")
#Phần 2 - Bài 11 : Tạo ma trận ngẫu nhiên trong phạm vi (1;10) và tính tổng đường chéo chính
def compute_trace():
    matrix = np.random.randint(1, 11, (3, 3))
    trace_1 = np.trace(matrix)

    trace_2 = 0
    for i in range(3):
        trace_2 += matrix[i, i]

    print(f"Random 3x3 matrix:\n{matrix}")
    print(f"Trace (by one command): {trace_1}")
    print(f"Trace (by loop): {trace_2}")

#Phần 2 - Bài 12 : Tạo ma trận với đường chéo chính lần lượt là 1,2,3
def create_diagonal_matrix():
    matrix = np.diag([1, 2, 3])
    print(f"Diagonal 3x3 matrix:\n{matrix}")

#Phần 2 - Bài 13 : Cho ma trận cho trước - tính định thức

def compute_determinant():
    A = np.array([[1, 1, 2], [2, 4, -3], [3, 6, -5]])
    determinant = np.linalg.det(A)
    print(f"Determinant of A: {determinant}")

#Phần 2 - Bài 14 : Tạo ma trận M từ 2 vecto a và b cho trước
def create_matrix_M():
    a1 = np.array([1, -2, -5])
    a2 = np.array([2, 5, 6])
    M = np.column_stack((a1, a2))
    print(f"Matrix M:\n{M}")

#Phần 2 - Bài 15 : Vẽ đồ thị y^2 với y nằm trong khoảng [-5;6]
def plot_square_y():
    y = np.arange(-5, 6)
    plt.plot(y, y**2, marker='o')
    plt.xlabel("y")
    plt.ylabel("y^2")
    plt.title("Plot of y^2")
    plt.grid(True)
    plt.show()
#Phần 2 - Bài 16 : Tạo 4 giá trị cách đều từ [0;32] tính cả 2 điểm đầu và cuối
def create_evenly_spaced():
    values = np.linspace(0, 32, 4)
    print(f"4 evenly spaced values: {values}")

#Phần 2 - Bài 17 : Lấy 50 giá trị cách đều trong khoảng [-5;5] cho x . Tính y^2 và vẽ đồ thị (x,y)
def plot_x_squared():
    x = np.linspace(-5, 5, 50)
    y = x**2
    plt.plot(x, y, label="y = x^2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Plot of y = x^2")
    plt.legend()
    plt.grid(True)
    plt.show()
#Phần 2 - Bài 18 : Vẽ đồ thị hàm số y = e^x kèm tiêu đề và nhãn trục

def plot_exp():
    x = np.linspace(-2, 2, 50)
    y = np.exp(x)
    plt.plot(x, y, label="y = e^x", color="green")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Exponential Function y = e^x")
    plt.legend()
    plt.grid(True)
    plt.show()

#Phần 2 - Bài 19 : Vẽ đồ th y = log(x) với  x từ [0;5]

def plot_log():
    x = np.linspace(0.1, 5, 50)  # Tránh log(0)
    y = np.log(x)
    plt.plot(x, y, label="y = log(x)", color="red")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Logarithm Function y = log(x)")
    plt.legend()
    plt.grid(True)
    plt.show()
#Phần 2 - Bài 20 : Chia thành 2 câu
# - Vẽ 2 biểu đồ y = e^x và y = e^2x trên cùng 1 biểu đồ
# - Vẽ y = log(x) và y = log(2x) trên cùng 1 subplot
def plot_exp_functions():
    x = np.linspace(-2, 2, 100)
    y1 = np.exp(x)
    y2 = np.exp(2*x)

    plt.plot(x, y1, label="y = exp(x)", color="blue")
    plt.plot(x, y2, label="y = exp(2x)", color="red")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Exponential Functions")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_log_functions():
    x = np.linspace(0.1, 10, 100)  # Tránh log(0)
    y1 = np.log(x)
    y2 = np.log(2*x)

    fig, ax = plt.subplots()
    ax.plot(x, y1, label="y = log(x)", color="green")
    ax.plot(x, y2, label="y = log(2x)", color="purple")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Logarithm Functions")
    ax.legend()
    ax.grid(True)
    plt.show()
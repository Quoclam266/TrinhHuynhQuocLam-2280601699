
093_ Lê Nguyễn Hoài Ngọc
09:41 (0 phút trước)
đến tôi

class RailFenceCipher:
    def __init__(self):
        pass

    def railfence_encrypt(self, plain_text, key):
        """
        Mã hóa văn bản bằng thuật toán Rail Fence Cipher.
        :param plain_text: Văn bản gốc cần mã hóa
        :param key: Số lượng rail (hàng) - phải là số nguyên >= 2
        :return: Văn bản đã mã hóa
        """
        if not plain_text or key < 2:
            return plain_text

        # Tạo ma trận rail
        rail = [''] * key
        row = 0
        direction = 1  # 1: đi xuống, -1: đi lên

        # Đặt các ký tự vào ma trận rail
        for char in plain_text:
            rail[row] += char
            row += direction
            if row == key:
                row = key - 2
                direction = -1
            elif row == -1:
                row = 1
                direction = 1

        # Kết hợp các rail để tạo văn bản mã hóa
        encrypted_text = ''.join(rail)
        return encrypted_text

    def railfence_decrypt(self, cipher_text, key):
        """
        Giải mã văn bản bằng thuật toán Rail Fence Cipher.
        :param cipher_text: Văn bản đã mã hóa
        :param key: Số lượng rail (hàng) - phải là số nguyên >= 2
        :return: Văn bản đã giải mã
        """
        if not cipher_text or key < 2:
            return cipher_text

        # Tạo mảng để đánh dấu vị trí các ký tự trong ma trận rail
        length = len(cipher_text)
        rail = [['\0'] * length for _ in range(key)]
        row = 0
        direction = 1
        index = 0

        # Đánh dấu vị trí các ký tự trong ma trận
        for i in range(length):
            rail[row][i] = '*'
            row += direction
            if row == key:
                row = key - 2
                direction = -1
            elif row == -1:
                row = 1
                direction = 1

        # Điền các ký tự từ cipher_text vào ma trận
        pos = 0
        for i in range(key):
            for j in range(length):
                if rail[i][j] == '*' and pos < length:
                    rail[i][j] = cipher_text[pos]
                    pos += 1

        # Đọc ma trận theo mẫu zig-zag để giải mã
        decrypted_text = ''
        row = 0
        direction = 1
        for i in range(length):
            decrypted_text += rail[row][i]
            row += direction
            if row == key:
                row = key - 2
                direction = -1
            elif row == -1:
                row = 1
                direction = 1

        return decrypted_text
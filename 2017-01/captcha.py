# First assignment from 2017 to see if everything is set up correctly :-)


def calculate_captcha_sum(digits, step=1):
    digit_sum = 0
    for i in range(0, len(digits)):
        if digits[i % len(digits)] == digits[(i + step) % len(digits)]:
            digit_sum += int(digits[i % len(digits)])
    return digit_sum


def calculate_advanced_captcha_sum(digits):
    return calculate_captcha_sum(digits, int(len(digits) / 2))

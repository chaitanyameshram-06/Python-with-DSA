
# ---------------- BASIC PROGRAMMING FUNCTIONS ----------------

def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c


def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"


def factorial(n):
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i
        i += 1
    return fact


def print_numbers(n):
    for i in range(1, n+1):
        print(i)


def count_even_odd(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s


def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)


def leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def largest_list(lst):
    largest = lst[0]
    for i in lst:
        if i > largest:
            largest = i
    return largest


def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count


def vote(age):
    if age >= 18:
        return "Eligible"
    else:
        return "Not Eligible"


def second_largest(lst):
    lst = list(set(lst))
    lst.sort()
    return lst[-2]


def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s


def password_strength(pw):
    if len(pw) >= 8:
        if any(c.isdigit() for c in pw):
            return "Strong"
        else:
            return "Medium"
    else:
        return "Weak"


def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def divisible(n):
    if n % 3 == 0 and n % 5 == 0:
        return True
    else:
        return False


def word_count(sentence):
    words = sentence.split()
    return len(words)


# ---------------- REAL-LIFE APPLICATION FUNCTIONS ----------------

def insta_count(n):
    if n >= 1000:
        return str(n//1000) + "K"
    return str(n)


def youtube_views(n):
    if n >= 1000000:
        return str(n//1000000) + "M"
    elif n >= 1000:
        return str(n//1000) + "K"
    else:
        return str(n)


def swiggy_status(minutes):
    if minutes < 10:
        return "Preparing"
    elif minutes < 30:
        return "On the way"
    else:
        return "Delivered"


def cart_total(prices):
    total = 0
    for p in prices:
        total += p
    return total


def upi_payment(balance, amount):
    if balance >= amount:
        return "Payment Successful"
    else:
        return "Insufficient Balance"


def netflix_hours(minutes):
    return minutes / 60


def surge_price(base, traffic):
    if traffic == "high":
        return base * 1.5
    elif traffic == "medium":
        return base * 1.2
    else:
        return base


def last_seen(minutes):
    if minutes < 1:
        return "Online"
    else:
        return str(minutes) + " minutes ago"


def battery_status(level):
    if level > 80:
        return "Full"
    elif level > 30:
        return "Medium"
    else:
        return "Low"


def fitness_goal(steps):
    if steps >= 10000:
        return "Goal Completed"
    else:
        return "Goal Not Completed"


def countdown(n):
    while n >= 0:
        print(n)
        n -= 1


def cashback(amount):
    return amount * 0.05


def delivery_time(distance):
    return distance / 40


def clothes(temp):
    if temp < 15:
        return "Jacket"
    elif temp < 25:
        return "Sweater"
    else:
        return "T-shirt"


def attendance(percent):
    if percent >= 75:
        return "Allowed"
    else:
        return "Shortage"


def fraud(amount):
    if amount > 50000:
        return "Possible Fraud"
    else:
        return "Normal"


def data_usage(used, limit):
    if used > limit * 0.8:
        return "High Usage"
    else:
        return "Normal"


def seat_status(seats):
    if seats > 0:
        return "Available"
    else:
        return "Waiting List"


def eta(distance, speed):
    return distance / speed


def food_rating(stars):
    return "Rating: " + str(stars) + "/5"


# ---------------- MISCELLANEOUS ----------------

def tip_reminder(bill):
    return bill * 0.05


def gmail_storage(used, total):
    if used / total > 0.9:
        return "Storage Almost Full"
    else:
        return "Storage OK"


def health_status(hp):
    if hp > 70:
        return "Healthy"
    elif hp > 30:
        return "Injured"
    else:
        return "Critical"


def speed_check(speed):
    if speed > 80:
        return "Over Speeding"
    else:
        return "Normal"


def follower_growth(old, new):
    if new > old:
        return "Growth"
    elif new == old:
        return "No Change"
    else:
        return "Decline"


def laptop_temp(temp):
    if temp > 85:
        return "Overheating"
    else:
        return "Normal"


def streak(days):
    return "Streak: " + str(days) + " days"


def simple_interest(p, r, t):
    return (p * r * t) / 100


def restaurant_bill(amount):
    return amount + amount * 0.18


def present_count(lst):
    count = 0
    for i in lst:
        if i.lower() == "present":
            count += 1
    return count

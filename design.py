# design.py

def print_success(text):
    # طباعة نص باللون الأخضر في الـ Terminal
    print(f"\033[92m[✓] {text}\033[0m")

def print_error(text):
    # طباعة نص باللون الأحمر
    print(f"\033[91m[✗] {text}\033[0m")

def print_info(text):
    # طباعة نص باللون الأزرق
    print(f"\033[94m[*] {text}\033[0m")

def show_banner():
    print("=" * 50)
    print("      🚀 ENTERPRISE NETWORK MANAGEMENT SYSTEM      ")
    print("=" * 50)

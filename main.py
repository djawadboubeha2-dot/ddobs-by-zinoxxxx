# main.py
import asyncio
import design   # استيراد نظام التصميم الخاص بنا
import network  # استيراد نظام الشبكة الخاص بنا

async def start_system():
    # 1. عرض الواجهة
    design.show_banner()
    
    # 2. أخذ المدخلات
    target = input("Enter target IP (e.g., 127.0.0.1): ")
    design.print_info(f"Starting analysis on {target}...\n")
    
    # المنافذ الهامة التي نريد فحصها
    important_ports = [21, 22, 80, 443, 3306, 8000]
    
    # 3. تشغيل الفحص المتوازي
    for port in important_ports:
        is_open = await network.check_single_port(target, port)
        
        if is_open:
            design.print_success(f"Port {port} is OPEN and active!")
        else:
            design.print_error(f"Port {port} is closed or secured.")

    print("\n" + "=" * 50)
    design.print_info("System analysis completed successfully.")

if __name__ == "__main__":
    # تشغيل النظام الرئيسي
    asyncio.run(start_system())

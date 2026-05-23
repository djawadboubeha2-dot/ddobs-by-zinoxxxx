# network.py
import asyncio

async def check_single_port(ip, port):
    try:
        # محاولة فتح اتصال سريع جداً
        conn = asyncio.open_connection(ip, port)
        reader, writer = await asyncio.wait_for(conn, timeout=0.5)
        writer.close()
        await writer.wait_closed()
        return True # المنفذ مفتوح
    except:
        return False # المنفذ مغلق

import streamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")

price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)

 net_price = price - vat

  st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")

st.divider()
st.write(" นางสาววรดา พึ่งตน เลขที่ 14 ม.4/4")

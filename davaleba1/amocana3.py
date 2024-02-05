monitor_price = float(input("შეიყვანეთ მონიტორის ფასი: "))
system_block_price = float(input("შეიყვანეთ სისტემური ბლოკის ფასი: "))
keyboard_price = float(input("შეიყვანეთ კლავიატურის ფასი: "))
mouse_price = float(input("შეიყვანეთ მაუსის ფასი: "))
total_price = monitor_price + system_block_price + keyboard_price + mouse_price
rounded_price = round(total_price, 2)
print("კომპიუტერის ღირებულებაა:", rounded_price)

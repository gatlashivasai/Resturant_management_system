def generate_bill(total):
    gst = total * 0.05
    final_amount = total + gst

    print("\n----- BILL -----")
    print("Total Amount :", total)
    print("GST (5%) :", gst)
    print("Final Amount :", final_amount)
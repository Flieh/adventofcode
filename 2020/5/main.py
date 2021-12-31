def main():
    f = open('input.txt','r')
    # f = open('sample_data.txt','r')
    records = f.read().split()
    highest_seat = 0 
    seating_list = []
    for rec in records:
        row = rec[:7]
        seat = rec[7:]
        tally = 0
        row = int(row.replace('F','0').replace('B','1'), 2)
        seat = int(seat.replace('L','0').replace('R','1'), 2)
        xid = row * 8 + seat
        if xid > highest_seat:
            highest_seat = xid
        seating_list.append(xid)
    first_seat = sorted(seating_list)[0]
    last_seat = sorted(seating_list)[-1]
    for seat in range(first_seat,last_seat):
        if seat not in seating_list:
            return seat

print(main())

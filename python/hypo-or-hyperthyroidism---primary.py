# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"1433.00","system":"readv2"},{"code":"212P.00","system":"readv2"},{"code":"66B4.00","system":"readv2"},{"code":"66BB.00","system":"readv2"},{"code":"66BZ.00","system":"readv2"},{"code":"8CR5.00","system":"readv2"},{"code":"9Oj..00","system":"readv2"},{"code":"9Oj3.00","system":"readv2"},{"code":"9Oj4.00","system":"readv2"},{"code":"C020200","system":"readv2"},{"code":"C040.00","system":"readv2"},{"code":"C041000","system":"readv2"},{"code":"C04z.00","system":"readv2"},{"code":"C04z.12","system":"readv2"},{"code":"C04z000","system":"readv2"},{"code":"C05z.00","system":"readv2"},{"code":"C06y100","system":"readv2"},{"code":"100004.0","system":"med"},{"code":"100476.0","system":"med"},{"code":"106532.0","system":"med"},{"code":"10760.0","system":"med"},{"code":"11146.0","system":"med"},{"code":"11322.0","system":"med"},{"code":"11426.0","system":"med"},{"code":"1346.0","system":"med"},{"code":"14704.0","system":"med"},{"code":"1472.0","system":"med"},{"code":"15565.0","system":"med"},{"code":"1567.0","system":"med"},{"code":"15790.0","system":"med"},{"code":"1619.0","system":"med"},{"code":"18282.0","system":"med"},{"code":"19205.0","system":"med"},{"code":"19367.0","system":"med"},{"code":"20035.0","system":"med"},{"code":"20310.0","system":"med"},{"code":"20909.0","system":"med"},{"code":"23014.0","system":"med"},{"code":"23315.0","system":"med"},{"code":"24748.0","system":"med"},{"code":"25913.0","system":"med"},{"code":"26362.0","system":"med"},{"code":"26699.0","system":"med"},{"code":"26701.0","system":"med"},{"code":"26702.0","system":"med"},{"code":"26833.0","system":"med"},{"code":"26869.0","system":"med"},{"code":"273.0","system":"med"},{"code":"28530.0","system":"med"},{"code":"28735.0","system":"med"},{"code":"28822.0","system":"med"},{"code":"28852.0","system":"med"},{"code":"3194.0","system":"med"},{"code":"31971.0","system":"med"},{"code":"3290.0","system":"med"},{"code":"34220.0","system":"med"},{"code":"3436.0","system":"med"},{"code":"35608.0","system":"med"},{"code":"3611.0","system":"med"},{"code":"3857.0","system":"med"},{"code":"38976.0","system":"med"},{"code":"3941.0","system":"med"},{"code":"43136.0","system":"med"},{"code":"44405.0","system":"med"},{"code":"46057.0","system":"med"},{"code":"46630.0","system":"med"},{"code":"46640.0","system":"med"},{"code":"46985.0","system":"med"},{"code":"47521.0","system":"med"},{"code":"47658.0","system":"med"},{"code":"47695.0","system":"med"},{"code":"48167.0","system":"med"},{"code":"49334.0","system":"med"},{"code":"49361.0","system":"med"},{"code":"4937.0","system":"med"},{"code":"50275.0","system":"med"},{"code":"51273.0","system":"med"},{"code":"51416.0","system":"med"},{"code":"51706.0","system":"med"},{"code":"5257.0","system":"med"},{"code":"53280.0","system":"med"},{"code":"53981.0","system":"med"},{"code":"56722.0","system":"med"},{"code":"57011.0","system":"med"},{"code":"59702.0","system":"med"},{"code":"61069.0","system":"med"},{"code":"61498.0","system":"med"},{"code":"6245.0","system":"med"},{"code":"65444.0","system":"med"},{"code":"65907.0","system":"med"},{"code":"677.0","system":"med"},{"code":"68512.0","system":"med"},{"code":"68626.0","system":"med"},{"code":"69113.0","system":"med"},{"code":"70244.0","system":"med"},{"code":"72690.0","system":"med"},{"code":"73107.0","system":"med"},{"code":"8038.0","system":"med"},{"code":"8268.0","system":"med"},{"code":"85661.0","system":"med"},{"code":"85955.0","system":"med"},{"code":"95335.0","system":"med"},{"code":"95885.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hypo-or-hyperthyroidism-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hypo-or-hyperthyroidism---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hypo-or-hyperthyroidism---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hypo-or-hyperthyroidism---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

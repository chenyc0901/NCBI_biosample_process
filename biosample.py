import re
import pandas as pd

def main():
    with open('biosample.txt','r') as f:
        result = {}
        total_result = []
        for line in f:
            line = line.strip()
            if line == '':
                total_result.append(result)
                result = {}
            else:
                if re.match('^\d{0,3}:.*',line):
                    match = re.search('Sample (.*)',line)
                    result['Sample'] = match.group(1)
                elif line.startswith('Identifiers'):
                    match = re.search('BioSample: (.*[^;]+);',line)
                    result['BioSample'] = match.group(1)
                    match = re.search('SRA: (.*)', line)
                    result['SRA'] = match.group(1)
                elif re.match('/.*',line):
                    atrribute = attribute_parser(line)
                    result.update(atrribute)
    df = pd.DataFrame(total_result)
    df = df.dropna(how='all')
    df.to_csv('result.csv',index=False)

def attribute_parser(line)->dict:
    parser = {}
    name, value = line.split("=")
    name = name[1:]
    value = value[1:-1]
    parser[name] = value 
    return parser




if __name__ == '__main__':
    main()
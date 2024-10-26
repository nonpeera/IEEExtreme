import csv
import sys
from collections import defaultdict

def read_records():
    records = []
    # Read CSV records from standard input
    print("Enter CSV records (type 'END' to finish):")
    
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        records.append(line)
    
    return records

def process_records(records):
    events = []
    parent_events = {}
    child_events = defaultdict(list)

    # Read and parse records
    for record in records:
        fields = list(csv.reader([record]))[0]
        if len(fields) != 6:
            continue  # Skip invalid records

        event_id, event_title, acronym, project_code, three_digit_code, record_type = fields
        
        # Create an event dictionary
        event = {
            'event_id': event_id,
            'event_title': event_title,
            'acronym': acronym,
            'project_code': project_code,
            'three_digit_code': three_digit_code,
            'record_type': record_type
        }
        
        if record_type == "Parent Event":
            parent_events[event_id] = event
        elif record_type == "IEEE Event":
            child_events[event_id].append(event)
        else:
            continue  # Invalid record type

    # Filter and construct output
    output = []
    excluded_ids = []
    
    for parent_id, parent in parent_events.items():
        children = child_events[parent_id]
        
        # Exclude parents without children
        if not children:
            excluded_ids.append(parent_id)
            continue
        
        # Check if all children have the same acronym
        unique_acronyms = {child['acronym'] for child in children}
        if len(unique_acronyms) != 1 or '' in unique_acronyms:
            excluded_ids.append(parent_id)
            continue
        
        # Determine 3 Digit Project Code
        project_codes = {child['three_digit_code'] for child in children if child['three_digit_code']}
        if len(project_codes) == 1:
            parent['three_digit_code'] = project_codes.pop()
        else:
            parent['three_digit_code'] = '???'
        
        # Add valid parent to output
        output.append(parent)  
        
        # Add children to output
        for child in children:
            output.append({**child, 'parent_id': parent_id})

    # Sort output by acronym, then title, then event_id
    output.sort(key=lambda x: (x['acronym'], x['event_title'], x['event_id']))
    
    return output, excluded_ids

def print_output(output, excluded_ids):
    for event in output:
        parent_id = event.get('parent_id')
        if parent_id:
            print(f"{event['event_id']},{event['event_title']},{event['acronym']},,{event['project_code']}," +
                  f"{event['three_digit_code']},\"IEEE Event\",{parent_id}")
        else:
            print(f"{event['event_id']},{event['event_title']},{event['acronym']},,{event['project_code']}," +
                  f"{event['three_digit_code']},\"Parent Event\"")
    
    if excluded_ids:
        print("\nThe excluded events' IDs are:")
        print(", ".join(excluded_ids))

def main():
    records = read_records()
    output, excluded_ids = process_records(records)
    print_output(output, excluded_ids)

if __name__ == "__main__":
    main()

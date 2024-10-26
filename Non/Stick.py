def calculate_union_area(N, K, L):
    events = []  # Stores events for the start and end of each square

    # Generate the events for all squares
    for i in range(N):
        x_start = i * K - L
        x_end = i * K + L
        y_start = i * K - L
        y_end = i * K + L
        events.append((x_start, y_start, y_end, 1))  # Square starts
        events.append((x_end, y_start, y_end, -1))   # Square ends

    # Sort events by x coordinate, breaking ties by type (start before end)
    events.sort()

    # Active y-intervals and their counts
    from collections import defaultdict
    active_intervals = defaultdict(int)
    prev_x = None
    total_area = 0
    active_length = 0

    def update_active_length():
        """Updates the total active length of y-intervals."""
        nonlocal active_length
        sorted_keys = sorted(active_intervals.keys())
        active_length = 0
        curr_start = None
        curr_count = 0

        for key in sorted_keys:
            if curr_start is not None and curr_count > 0:
                active_length += key - curr_start
            curr_start = key
            curr_count += active_intervals[key]

    # Process the sorted events
    for x, y_start, y_end, event_type in events:
        if prev_x is not None and active_length > 0:
            # Add the area covered between prev_x and x
            total_area += active_length * (x - prev_x)

        # Update active intervals
        active_intervals[y_start] += event_type
        active_intervals[y_end] -= event_type

        # Recompute active length
        update_active_length()

        # Update previous x position
        prev_x = x

    return total_area

# Input reading
N, K, L = map(int, input().split())

# Calculate the area of the union of the squares
result = calculate_union_area(N, K, L)

# Output the result
print(result)

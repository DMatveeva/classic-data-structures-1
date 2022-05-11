def rotate_queue(queue, n):
    remainder = n % queue.size()
    if remainder == 0:
        return
    i = 0
    while i < queue.size() - remainder:
        queue.enqueue(queue.dequeue())
        i += 1

def rotate_queue(queue, n):
    i = n % queue.size() - queue.size()
    while i < 0:
        queue.enqueue(queue.dequeue())
        i += 1

def rotate_queue(queue, n):
    i = 0 if n % queue.size() == 0 else n % queue.size() - queue.size()
    while i < 0:
        queue.enqueue(queue.dequeue())
        i += 1

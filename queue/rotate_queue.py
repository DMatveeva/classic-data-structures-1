def rotate_queue(queue, n):
    while n % queue.size() > 0:
        queue.enqueue(queue.dequeue())
        n -= 1

from queue.Queue import Queue


def rotate_queue(queue, n):
    remainder = n % queue.size()
    if remainder == 0:
        return
    i = 0
    while i < queue.size() - remainder:
        element = queue.dequeue()
        queue.enqueue(element)
        i += 1

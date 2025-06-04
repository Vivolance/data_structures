from queue import Queue
from threading import Thread, Event


class S3BackgroundThread(Thread):
    def __init__(
        self, queue: Queue
    ) -> None:
        """
        Background thread that batches and uploads to S3
        """
        super().__init__()
        self._queue: Queue = queue
        self._shutdown_event: Event = Event()

    def run(self):
        while not self._shutdown_event.is_set():
            print("S3UploaderThread: Running...")

    def stop(self) -> None:
        self._shutdown_event.set()


class Orchestrator:
    def __init__(self):
        self.queue: Queue = Queue()
        self.s3_explorer_thread: S3BackgroundThread = S3BackgroundThread(
            queue=self.queue
        )

    def run(self):
        # start calls the run() method
        self.s3_explorer_thread.start()


if __name__ == "__main__":
    orchestrator: Orchestrator = Orchestrator()
    orchestrator.run()
    for _ in range(10):
        print("Main Thread: Running...")
    orchestrator.s3_explorer_thread.stop()
    print("S3ExplorerThread Stop signal sent")
    # waits until background thread finishes before ending main thread
    orchestrator.s3_explorer_thread.join()
    print("Main Thread: S3 Explorer Thread has stopped and cleaned up")

import logging
import random
import sys
import time
from typing import Callable

from PyQt5.QtCore import QRunnable, Qt, QThreadPool
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class Runnable(QRunnable):
    def __init__(self, task: Callable, delay: float):
        super().__init__()
        self.delay = delay
        self.task = task

    def run(self):
        time.sleep(self.delay)
        self.task()


class Sleeper:
    @staticmethod
    def run_after_delay(task: Callable, delay: float):
        pool = QThreadPool.globalInstance()
        runnable = Runnable(task, delay)
        pool.start(runnable)

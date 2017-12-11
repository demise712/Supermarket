FROM python

RUN python test_register_supermarket.py

CMD ["python", "product_entry.py"]

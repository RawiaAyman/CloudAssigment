FROM python

# Set the working directory in the container
WORKDIR /app
 

# Copy the current directory contents into the container at /app
COPY pythonapp.py /app/
COPY paragraphs.txt /app/

# Install any needed packages specified in requirements.txt

RUN pip install --no-cache-dir nltk && \
    python -m nltk.downloader stopwords punkt

# Run the Python script when the container launches
CMD ["python", "pythonapp.py"]
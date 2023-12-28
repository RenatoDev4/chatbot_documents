from typing import List, Tuple

import PyPDF2


def read_and_textify(files: List[str]) -> Tuple[List[str], List[str]]:
    """
    Read and extract text from PDF files.

    Args:
        files (List[str]): List of file paths.

    Returns:
        Tuple[List[str], List[str]]: A tuple containing two lists.
            The first list contains the extracted text from each page of the PDF files.
            The second list contains the source file name and page number for each extracted text.
    """
    text_list = []
    sources_list = []
    for file in files:
        pdfReader = PyPDF2.PdfReader(file)
        for i in range(len(pdfReader.pages)):
            pageObj = pdfReader.pages[i]
            text = pageObj.extract_text()
            pageObj.clear()
            text_list.append(text)
            sources_list.append(file.name + "_page_"+str(i))
    return text_list, sources_list

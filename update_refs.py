import re

with open('/home/i/Desktop/Pedro/Universidade/3-2/IAA/paper/paper.tex', 'r') as f:
    content = f.read()

replacements = [
    (r'they cannot handle null or undefined values\.', r'they cannot handle null or undefined values \cite{ahmad2024impact}.'),
    (r'(\n\\noindent \\textbf{Definition:} The missingness of data has no relationship with any values in the dataset, whether observed or missing\. It is entirely random\.)', r'\1 \cite{kang2013prevention}'),
    (r'(\n\\noindent \\textbf{Definition:} The missingness is systematic, but can be explained by other observed variables in the dataset\. It is not dependent on the missing value itself\.)', r'\1 \cite{kang2013prevention}'),
    (r'(\n\\noindent \\textbf{Definition:} The missingness is directly related to the value that is missing\. The absence of data is a signal in itself\. This is the most difficult scenario to handle\.)', r'\1 \cite{kang2013prevention}'),
    (r'(\n\\noindent \\textbf{Real-World Example:} A lab sample is accidentally dropped and destroyed, or a printing error causes a survey page to be skipped\.)', r'\1 \cite{zhou2024comprehensive}'),
    (r'(\n\\noindent \\textbf{Real-World Example:} Older patients \(an observed variable\) are less likely to have a specific invasive test\. The missing test result is related to age, not the result of the test\.)', r'\1 \cite{zhou2024comprehensive}'),
    (r'(\n\\noindent \\textbf{Real-World Example:} High-income earners refusing to disclose their salary \(missingness is driven by the high salary\) or heavy smokers hiding their smoking habits\.)', r'\1 \cite{zhou2024comprehensive}'),
    (r'(\n\\noindent \\textbf{Method:} The default for plenty of legacy systems\. Involves removing an entire row \(observation\) if it has even a single missing value\.)', r'\1 \cite{meng2025comparative}'),
    (r'we would discard most data from your dataset\.', r'we would discard most data from your dataset \cite{chen2022handling}.'),
    (r'that rely on matrix inversion or stable eigenspaces\.', r'that rely on matrix inversion or stable eigenspaces \cite{cohen2026methods}.'),
    (r'This gives a false sense of statistical confidence and leads to poor real-world generalization\.', r'This gives a false sense of statistical confidence and leads to poor real-world generalization \cite{meng2025comparative}.'),
    (r'In volatile environments, this assumption is mathematically invalid and produces heavily biased estimates\.', r'In volatile environments, this assumption is mathematically invalid and produces heavily biased estimates \cite{kang2013prevention}.'),
    (r'its time complexity scales quadratically \(\$O\(n\^2\)\$\), making it too slow for massive datasets\.', r'its time complexity scales quadratically ($O(n^2)$), making it too slow for massive datasets \cite{suh2023comparison}.'),
    (r'process the same data in a fraction of the time, mitigating these problems\.', r'process the same data in a fraction of the time, mitigating these problems \cite{suh2023comparison}.'),
    (r'(\n\\noindent \\textbf{Advantages:} It is biostatistical ``gold standard'' for unbiased estimates under the MAR assumption because it quantifies imputation uncertainty\.)', r'\1 \cite{austin2021missing}'),
    (r'allowed downstream models to achieve an astonishing F1-score of 0\.9435\.', r'allowed downstream models to achieve an astonishing F1-score of 0.9435 \cite{choi2025comparison}.'),
    (r'A monumental benchmarking study \(520,000 CPU hours\) proved', r'A monumental benchmarking study (520,000 CPU hours) \cite{lemorvan2022benchmarking} proved'),
    (r'inflating our confidence in the data and fooling ourselves\.', r'inflating our confidence in the data and fooling ourselves. Furthermore, explicit imputation models inherently learn the statistical patterns of the dominant majority, frequently skewing the decision boundary against marginalized groups and introducing algorithmic unfairness \cite{caton2022impact}.')
]

for old, new in replacements:
    content = re.sub(old, new, content, count=1)

bib_old = r'\\begin\{thebibliography\}\{00\}.*?\\end\{thebibliography\}'
bib_new = r'''\\begin{thebibliography}{00}

\\bibitem{ahmad2024impact}
A. F. Ahmad, M. S. Sayeed, K. Alshammari, and I. Ahmed, ``Impact of Missing Values in Machine Learning: A Comprehensive Analysis,'' \\textit{arXiv preprint arXiv:2410.08295}, 2024. [Online]. Available: \\url{https://arxiv.org/abs/2410.08295}

\\bibitem{kang2013prevention}
H. Kang, ``The prevention and handling of the missing data,'' \\textit{Korean J. Anesthesiol.}, vol. 64, no. 5, pp. 402--406, May 2013. [Online]. Available: \\url{https://pmc.ncbi.nlm.nih.gov/articles/PMC3668100/}

\\bibitem{zhou2024comprehensive}
Y. Zhou, S. Aryal, and M. R. Bouadjenek, ``A Comprehensive Review of Handling Missing Data: Exploring Special Missing Mechanisms,'' \\textit{arXiv preprint arXiv:2404.04905}, 2024. [Online]. Available: \\url{https://arxiv.org/html/2404.04905v1}

\\bibitem{meng2025comparative}
H. Meng, ``A Comparative Study on Missing Value Imputation Techniques in Machine Learning,'' \\textit{SHS Web of Conferences}, vol. 218, p. 02014, 2025. [Online]. Available: \\url{https://www.shs-conferences.org/articles/shsconf/pdf/2025/09/shsconf_icdde2025_02014.pdf}

\\bibitem{chen2022handling}
S. Chen and C. Xu, ``Handling high-dimensional data with missing values by modern machine learning techniques,'' \\textit{Journal of Applied Statistics}, vol. 50, no. 3, pp. 786--804, May 2022. [Online]. Available: \\url{https://pmc.ncbi.nlm.nih.gov/articles/PMC9930810/}

\\bibitem{cohen2026methods}
M. X. Cohen, ``13.4 Methods for Handling Missing Data,'' in \\textit{A Guide on Data Analysis}, Bookdown. [Online]. Available: \\url{https://bookdown.org/mike/data_analysis/methods-for-handling-missing-data.html}. [Accessed: Feb. 23, 2026].

\\bibitem{suh2023comparison}
H. Suh and J. Song, ``A comparison of imputation methods using machine learning models,'' \\textit{Commun. Stat. Appl. Methods}, vol. 30, no. 3, pp. 331--341, May 2023. [Online]. Available: \\url{http://www.csam.or.kr/journal/view.html?doi=10.29220/CSAM.2023.30.3.331}

\\bibitem{austin2021missing}
P. C. Austin, I. R. White, D. S. Lee, and S. van Buuren, ``Missing Data in Clinical Research: A Tutorial on Multiple Imputation,'' \\textit{Can. J. Cardiol.}, vol. 37, no. 9, pp. 1322--1331, Sep. 2021. [Online]. Available: \\url{https://pmc.ncbi.nlm.nih.gov/articles/PMC8499698/}

\\bibitem{choi2025comparison}
V. W.-C. Choi, ``Comparison of Data Imputation Performance in Deep Generative Models for Educational Tabular Missing Data,'' in \\textit{Proc. 18th Int. Conf. Educ. Data Mining (EDM)}, 2025. [Online]. Available: \\url{https://educationaldatamining.org/EDM2025/proceedings/2025.EDM.long-papers.17/}

\\bibitem{lemorvan2022benchmarking}
M. Le Morvan \\textit{et al.}, ``Benchmarking missing-values approaches for predictive models on health databases,'' \\textit{GigaScience}, vol. 11, p. giac013, Apr. 2022. [Online]. Available: \\url{https://pmc.ncbi.nlm.nih.gov/articles/PMC9012100/}

\\bibitem{caton2022impact}
S. Caton, S. Malisetty, and C. Haas, ``Impact of Imputation Strategies on Fairness in Machine Learning,'' \\textit{Journal of Artificial Intelligence Research}, vol. 74, pp. 1011--1035, Jul. 2022. [Online]. Available: \\url{https://jair.org/index.php/jair/article/view/13197}

\\end{thebibliography}'''

content = re.sub(bib_old, bib_new, content, flags=re.DOTALL)

with open('/home/i/Desktop/Pedro/Universidade/3-2/IAA/paper/paper.tex', 'w') as f:
    f.write(content)

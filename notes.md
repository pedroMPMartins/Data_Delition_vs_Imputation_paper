# Introduction
Missing data, how to handle it?
Removal vs Imputation


Datasets are never perfectly populated. We'll never have a perfect dataset, as it will, inevitably, have missing data and inconsistencies. They are inherently messy, include noise, systemic exclusions, lack of consistency and most notable, incomplete information. Data exploration and pre-processing are needed, and they must tackle the need to handle the missing data.
This is because the vast majority of machine learning algorithms are design strictly to operate on complete matrices, so they cannot handle null or undefined values.


# Missing types of data

## Missing Completely At Random (MCAR)

**Definition:** The missingness of data has **no relationshit** with any values in the dataset. Whether observed or missing. It is entirely random.

**Implication:** the remaining data is a statistically representative sample.

**Real-World Example:** a lab sample is accidentally dropped and destroyed, or a printing error causes a survey page to be skipped.


## Missing At Random (MAR)

**Definition:** the missingness is systematic, but can be explained by **other observed variables** in the dataset. It is not dependent on the missing value itself.

**Implication:** statistical relationships exist that allow us to predict the missing values.

**Real-World Example:** Older patients (an observed variable) are less likely to have a specific invasive test. The missing test result is related to age, not the result of the test.


## Missing Not At Random (MNAR)

**Definition:** the missingness is **directly related to the value that is missing**. The absence of data is a signal in itself. This is the most dangerous scenario.

**Implication:** the observed data lacks the information needed to predict the missing values. Standard imputation will fail and produce biased results.

**Real-World Example:** high-income earners refusing to disclose their salary (missingness is driven by the high salary) or heavy smokers hiding their smoking habits.



# Data Deletion Strategies

## Listwise Deletion (Complete Case Analysis)

__Method:__ the default for plenty of legacy systems. Involves removing an entire row (observation) if it has even a single missing value.

__When to use:__ it produces unbiased estimates **only** if the data is strictly **MCAR**

__Problems:__ in high-dimensional datasets (many columns), this method fails catastrophically.
For example, if you have 100 features with a 1% chance of having a value being missing, statistically, we would discard most data from your dataset.


## Pairwise Deletion (Available Case Analysis)

__Method:__ instead of deleting the whole row, this method uses all available data for specific pairs of variables. It is often used to calculate correlation or covariance matrices.

__Problem:__ it creates structural mathematical vulnerabilities. This is due to different parts of the matrix being calculated using different sample sizes, the resulting covariance matrix is often not positive definite. This mathematical inconsistency causes fatal errors in machine learning algorithms that rely on matrix inversion or stable eigenspaces.


## Column Deletion

__Method:__ removing an entire feature (column) rather than rows.

__When to use:__ generally, this is only viable if a feature has extreme missingness (e.g. more that 40% or 50%) and low predictive power. And it should also not be used in **MNAR**.

__Problem:__ risk of discarding "latent signals", especially in **MNAR** scenarios where the absence of the feature is a predictor in itself.



# Classical and Statistical Substitution

## Central Tendency Substitution

__Method:__ replacing missing numerical values with the mean or median, and categorical values with the mode (the value that appears most frequently in a dataset) or a constant like "Unknown".

__Appeal:__ extremely fast, computationally efficient, and scales effortlessly to massive datasets

__Problem:__ it artificially compresses the mathematical variance of the dataset. By replacing diverse missing values with a single static number, distortion of relationships (covariance) between features happens, as well as artificially lowers standard errors. This gives a false sense of statistical confidence and leads to poor real-word generalization.


## Longitudinal Carry-Forward (Last Observation Carried Forward or LOCF and Interpolation)

__Method:__ common in time-series, finance and clinical trials. **LOCF** replaces missing value with the most recent observed historical value. **Linear interpolation** draws a straight line between two known temporal points to guess the missing middle.

__Appeal:__ highly intuitive and easy to explain to non-technical stakeholders.

__Problem:__ relies on the dangerous assumption that dynamic systems remain entirely static between observations. In volatile environments, this assumption is mathematically invalid and produces heavily biased estimates.


## Regression-Based Imputation

__Method:__ using existing, complete variables to build a regression model that predicts and fills in the missing values

__Appeal:__ preserves the shape of the mathematical distribution much better that central tendency substitution and avoids outright data deletion.

__Problem:__ adds absolutely no novel information to the dataset. Because the new value is a perfect mathematical function on the other columns, it artificially inflates multi-collinearity (variables being to highly correlated). This creates an illusion of highly predictive power that will inevitably collapse when tested on new unseen data.



# Algorithmic Imputation

## Instance-Based Estimation: k-Nearest Neighbors (k-NN)

__Method:__ instance-based algorithm that finds the `k` most mathematically similar complete records (neighbors) using distance metrics like Euclidean or Hamming distance. It them fills the missing gap with the mean, median or mode of those neighbors.

__Advantage:__ empirical studies show it vastly outperforms simple deletion and substitution, preserving local data structures and boosting downstream model accuracy.

__Problem:__ it suffers from the "curse of dimensionality" (distance loses meaning as features increase) and is computationally exorbitant. This is due to the fact that it compares every single data point to every other data point, its time complexity scales quadratically (O(n^2)), making it too slow for massive datasets.


## Ensemble and Tree-Based Imputation (missForrest and mixgb)

__Method:__ uses tree-based algorithms (like Random Forests or XGBoost) to interatively predict missing values across all features.

__Advantage:__ natively handles complex, non-linear relationships and mixed data types (continuous and categorical) without extensive data scaling or strict distributional assumptions.

__Problem:__ traditional methods like missForrest are computationally heavy and require significant processing time. However, modern variants using chained forrests (missRanger) or XGBoost (mixgb) process the same data in a fraction of the time, mitigating these problems.


## Multiple Imputation by Chained Equations (MICE)

__Method:__ rooted in Bayesian statistics, MICE acknowledges that any single guess is inherently uncertain. Instead of one substituted value, it generates multiple simulated versions of the complete dataset, trains models on each independently and mathematically pools the results.

__Advantage:__ it is biostatistical "gold standard" for unbiased estimated under the MAR assumption because it quantifies imputation uncertainty.

__Problem:__ it is an engineering nightmare for production machine learning pipelines. Storing and processing multiple parallel datasets creates massive computational burdens and destroys the interpretability of standard models.

Primary Mathematical Approach,Key Technical Advantages,Primary Limitations and Bottlenecks
Statistical (Mean/Mode),Computationally instantaneous (O(n)); trivial to deploy.,Compresses variance; distorts covariance; biased under MAR/MNAR.
k-Nearest Neighbors,Preserves local structures; highly effective for mixed data types.,Computationally exorbitant (O(n2)); degrades in high dimensions.
Iterative Tree Ensembles (missForest),Natively handles non-linearities and categorical data; robust to outliers.,Massive computational cost for standard versions; high memory use.
Multiple Imputation (MICE),Quantifies uncertainty; statistically rigorous under MAR.,Extremely difficult to deploy in production; complex model pooling.



# Deep Learning and Diffusion Models for Imputation

__Method:__ as datasets frow massive, data scientists are turning to deep generative architectures like Variational Autoencoders, GANs, and specifically TabDDPM (Denoising Diffusion Probabilistic Models adapted for tabular data).
Originally built for image generation, diffusion models systematically add Gaussian noise to a dataset until it is pure entropy, then train a neural network to reverse the process. TabDDPM does this directly on incomplete data matrices to learn the underlying districution.

__Advantage:__ it is incredibly resilient under extreme missingness. In benchmarks with 40% to 60% missing data, it synthesized highly realistic distributions. Even in a catastrophic scenario where 80% of the data was missing, TabDDPM (combined with SMOTE) allowed downstream models to achieve an astonishing F1-score of 0.9435.

__Problem:__ it carries massive operational burdens. Training these models requires immense GPU resources, lots of time and hyper complex parameter tuning. Making their use a complete pipe dream, unless sufficient funding, resources and time is allocated. Rapid prototyping is also impossible.



# Native Algorithmic Handling of missing data
Instead of computationally exhausting resources and attempts trying to perfectly reconstruct missing data, simply use algorithms that are engineered to natively ingest incomplete data.

__Method:__ advanced gradient boosted decision trees (like **XGBoost** and **LightGBM**) use a strategy called **Missing Incorporated in Attributes (MIA)**. When building a decision tree, the algorithm dynamically tests whether sending all missing values down the left or right branch yields the best reduction in the loss function.

__Advantage:__ it organically learns the predictive value of the missingness itself. A monumental benchmarking study (520,000 CPU hours) proved that this native handling systematically outperforms state-of-the-art imputation (like MICE or k-NN) in both accuracy and speed.

__Why:__ real-word missing data is almost always informative (MNAR). Explicitly reconstructing missing values is frequently an unnecessary, computationally wasteful, and statistically suboptimal step for predictive modeling.

__Problem:__ model-specific. Does not actually "fill in" the data if it needs complete table for reporting









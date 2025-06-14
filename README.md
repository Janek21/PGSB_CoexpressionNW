⚠️Repository in developement⚠️
# PGSB_CoexpressionNW

_From the earth I rise and to the earth I shall return, alas while I still draw breath I will be eating corn_
---
This repository contains the files and data for executing a network co-expression analysis on maize lines B73, DK105, EP1, F7 and PE75.
It has programs for both of the the analysis done in my [internship](./programs/IndividualNetworks.Rmd) and in my bachelor thesis().

The original [expression data](./data/original_data) has been kept, but there is also the processed and split data (containing the gene [length](./data/wlen/) and without the gene [length](./data/nolen)), the mercator annotation data can also be found, as well as the data belonging to _Zea Mays_ genes and the [protein](./data/annotation/Zm-B73-REFERENCE-NAM-5.0_Zm00001eb.1.protein.fa) and [canonical](./data/annotation/Zm-B73-REFERENCE-NAM-5.0_Zm00001eb.1.canonical.cds.fa) sequences of this same species.

---
## [`Scripts`](./scripts) directory

Contains programs for the initial data analysis and pre-processing

[`Preliminary analysis`](./scripts/PreliminaryAnalysis.Rmd): R markdown for initial viewing of the data

[`Bash execution file`](./scripts/Preprocessing.sh): Executes all the steps for the initial data cleaning

* [`MetaFixer.R`](./scripts/MetaFixer.R): Matches the amount of samples to the lowest one among data and metadata
* [`tissue_abv.py`](./scripts/tissue_abv.py): Assigns to each metadata tissue code a tissue abreviation for a better comprehension.
* [`speciator.R`](./scripts/speciator.R): Splits the data and metadata tables by lines, necessary only for the internship project.

## [`Co-expression`](./coexpression_code) directory

Contains programs and results belonging to the co-expression network creation and analysis

[`IndividualNetworks.Rmd`](./coexpression_code/IndividualNetworks.Rmd): Co-expression network creation and correaltion analysis for individual lines.

[`WholeLineNetworks.Rmd`](./coexpression_code/WholeLineNetworks.Rmd): Co-expression network creation and correaltion analysis simultaneous for all lines.

[`geneModule.txt`](./coexpression_code/geneModule.txt): Table containing each gene and the module to which it belongs

[`Distribution plots`](./coexpression_code/DistrPlots): Contains the data distributions for the raw, normalized(through CPM and RPKM), filtered and unfiltered data.

[`Expression plots`](./coexpression_code/ExprPlots): Where PCA and UMAP data visualizations are saved

[`Correlation plots`](./coexpression_code/CorPlots): Contains the plots and tables where the module co-expression across tissues (and lines) is reflected.


## [`Annotation`](./annotation_code) directory

Contains programs and results which belong to functional annotation of both, modules and genes.

[`Module functions`](./annotation_code/modules): Contains the code and results for obtaining the main functions of modules

* [`FileRead_class.py`](./annotation_code/modules/FileRead_class.py): Classes for parsing files (mercator annotation [file](./data/annotationb73.mercator.v4.7.txt) and P-value [tables](./annotation_code/modules/Pres)).
* [`FunctionPval_tables.py`](./annotation_code/modules/FunctionPval_tables.py): Calculates the significance for functions in each module, saves them in [tables](./annotation_code/modules/Pres).
* [`SignificantPerModule_plots.R`](./annotation_code/modules/SignificantPerModule_plots.R): Plots the significance per function in each module and the top significant functions, saves them in a [directory](./annotation_code/modules/SigPlots).
* [`TopSignificantFunctions.py`](./annotation_code/modules/TopSignificantFunctions.py): Writes a [table](./annotation_code/modules/database.txt) of most significant functions in each module for each annotation type.
* [`Pres`](./annotation_code/modules/Pres): Tables containing function, significance and module for each annotation type, created with [FileRead_class.py](./annotation_code/modules/FileRead_class.py).
* [`SigPlots`](./annotation_code/modules/SigPlots): Contains plots and tables of significance per function in each module and of the top significant functions per annotation type, which are created using [SignificantPerModule_plots.R](./annotation_code/modules/SignificantPerModule_plots.R).


[`Gene functions`](./annotation_code/genes): Contains the code and results for obtaining the gene communities and annotations.

* [`maize.B73.AGPv4.aggregate.gaf`](./annotation_code/genes/maize.B73.AGPv4.aggregate.gaf): File containing GO term, taxon, evidence code and more data belonging to _Zea Mays_ genes.
* [`geneClustering.Rmd`](./annotation_code/genes/geneClustering.Rmd): Calculates and saves the correlation table and performs a K-means and DBscan clustering for a give module.
* [`GOparser_class.py`](./annotation_code/genes/GOparser_class.py): 



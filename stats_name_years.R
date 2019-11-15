#!/usr/bin/env Rscript

args = commandArgs(trailingOnly=TRUE);
if (length(args) != 1) {
 	 stop("Mauvais nombre de paramètres: stats_name_years.R <nomFichier> ");
}

data <- read.csv(args[1],header=TRUE);

name=strsplit(basename(args[1]),"[.]")[[1]][1];

pdf(file=paste(name,".pdf",sep=""));

barplot(data$nmovies, names.arg=data$year, main=name,xlab="Année",
											ylab="# films",las=2,cex.names=.5,axes=FALSE);
axis(2,at=min(data$nmovies):max(data$nmovies));
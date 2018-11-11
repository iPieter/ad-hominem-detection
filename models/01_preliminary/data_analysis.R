install.packages("dplyr")
install.packages("caret")
install.packages("tidyverse")
library(dplyr)
library(caret)
library(tidyverse)

# Get fallacies dataset
fallacies.df <- read.csv(file=file.choose(), header=TRUE, sep="\t")

cleaned_fallacies.df <- data.frame(fallacies.df$Topic, fallacies.df$Intended.Fallacy, fallacies.df$Text)
cleaned_fallacies.df <- cleaned_fallacies.df[-which((cleaned_fallacies.df$fallacies.df.Topic == "") | (cleaned_fallacies.df$fallacies.df.Intended.Fallacy == "") | (cleaned_fallacies.df$fallacies.df.Text == "")),]

cleaned_fallacies_sorted.df <- cleaned_fallacies.df[with(cleaned_fallacies.df, order(cleaned_fallacies.df$fallacies.df.Topic)),]

cleaned_fallacies_sorted.df <- cleaned_fallacies_sorted.df[which((cleaned_fallacies_sorted.df$fallacies.df.Intended.Fallacy=="Ad Hominem") | cleaned_fallacies_sorted.df$fallacies.df.Intended.Fallacy=="No Fallacy"),]
cleaned_fallacies_sorted.df <- mutate(cleaned_fallacies_sorted.df, Eric = "")
cleaned_fallacies_sorted.df <- mutate(cleaned_fallacies_sorted.df, Pieter = "")
cleaned_fallacies_sorted.df <- mutate(cleaned_fallacies_sorted.df, Murilo = "")

write_delim(cleaned_fallacies_sorted.df, "~/Projects/MAI/1st_semester/KTW/G0B34a_knowledge_and_the_web/data/general/ad_hominem_attacks.csv", delim = ",")
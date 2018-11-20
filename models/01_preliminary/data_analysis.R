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

ad_hominems.df <- data.frame(reddit_ad_hominem$body, reddit_ad_hominem$ad_hominem)
ad_hominems.df$reddit_ad_hominem.ad_hominem <- ifelse(ad_hominems.df$reddit_ad_hominem.ad_hominem == "True", 1, 0)

write_delim(ad_hominems.df, "~/Projects/MAI/1st_semester/KTW/G0B34a_knowledge_and_the_web/data/ad_hominem/ad_hominems_cleaned.csv", delim = ",")

ad_hominem_attacks_tmp <- ad_hominem_attacks[which(ad_hominem_attacks$Eric + ad_hominem_attacks$Pieter + ad_hominem_attacks$Murilo >= 2), ]

general_ad_hominems <- data.frame(ad_hominem_attacks_tmp$fallacies.df.Text, ad_hominem_attacks_tmp$fallacies.df.Intended.Fallacy)
general_ad_hominems$ad_hominem_attacks_tmp.fallacies.df.Intended.Fallacy <- ifelse(general_ad_hominems$ad_hominem_attacks_tmp.fallacies.df.Intended.Fallacy == "Ad Hominem", 1, 0)

write_delim(ad_hominems.df, "~/Projects/MAI/1st_semester/KTW/G0B34a_knowledge_and_the_web/data/general/general_dataset_cleaned.csv", delim = ",")

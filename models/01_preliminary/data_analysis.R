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


ad_hominem_attacks.sub <- cleaned_fallacies.df[grep("Ad Hominem", cleaned_fallacies.df$fallacies.df.Intended.Fallacy),]
ad_hominem_attacks.sub <- mutate(ad_hominem_attacks.sub, NegativeExample = "")

non_fallacies.sub <- cleaned_fallacies.df[grep("No Fallacy", cleaned_fallacies.df$fallacies.df.Intended.Fallacy),]

write.csv(non_fallacies.sub, "~/Projects/MAI/1st_semester/KTW/G0B34a_knowledge_and_the_web/data/general/non_fallacies.csv")
write.csv(ad_hominem_attacks.sub, "~/Projects/MAI/1st_semester/KTW/G0B34a_knowledge_and_the_web/data/general/ad_hominem_attacks.csv")
library(ggplot2)

os_data <- data.frame(
  OS = c("Windows", "OS X", "Unknown", "Linux", "Chrome OS", "FreeBSD"),
  MarketShare = c(72.52, 14.68, 6.47, 4.05, 2.27, 0.01)
)

ggplot(os_data, aes(x = OS, y = MarketShare, fill = OS)) +
  geom_bar(stat = "identity", color = "black") +
  geom_text(aes(label = paste0(MarketShare, "%")), vjust = -0.5) +
  labs(
    title = "Operating System Market Share Worldwide (2024)",
    x = "Operating System",
    y = "Market Share (%)"
  ) +
  theme_minimal() +
  theme(legend.position = "none")
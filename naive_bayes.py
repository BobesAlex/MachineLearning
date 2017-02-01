def train(category, text)
  each_word(text) {|w| increment_word(w, category) }
  increment_cat(category)
end
def classify(text, default=nil)
  max_prob = 0.0
  best = nil
  scores = cat_scores(text)
  scores.each do |score|
    cat, prob = score
    if prob > max_prob
      max_prob = prob
      best = cat
    end
  end
  return default unless best
  threshold = @thresholds[best] || 1.0
  scores.each do |score|
    cat, prob = score
    next if cat == best
    return default if prob * threshold > max_prob
  end
  return best
end

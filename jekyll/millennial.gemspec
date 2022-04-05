# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name          = "my-website"
  spec.version       = "0.1.0"
  spec.authors       = ["Elias Maier"]
  spec.email         = ["maierelias13@gmail.com"]

  spec.summary       = "A static wabsite for my GitHub Pages"
  spec.homepage      = "https://eeli1.github.io/"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(assets|_layouts|_includes|_sass|LICENSE|README|CHANGELOG)!i) }

  spec.add_runtime_dependency "jekyll", "~> 4.2"
  spec.add_runtime_dependency "jekyll-feed", "~> 0.6"
  spec.add_runtime_dependency "jekyll-paginate", "~> 1.1"
  spec.add_runtime_dependency "jekyll-sitemap", "~> 1.3"
  spec.add_runtime_dependency "jekyll-seo-tag", "~> 2.6"

end

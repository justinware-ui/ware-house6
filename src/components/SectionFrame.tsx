type SectionFrameProps = {
  title: string
  htmlPath: string
}

export default function SectionFrame({ title, htmlPath }: SectionFrameProps) {
  return (
    <section className="h-full min-h-0 bg-white">
      <iframe title={title} src={htmlPath} className="h-full w-full border-0" />
    </section>
  )
}

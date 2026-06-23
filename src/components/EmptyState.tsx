export default function EmptyState() {
  return (
    <section className="flex h-full items-center justify-center p-8">
      <div className="max-w-lg rounded-2xl border border-black/10 bg-white p-8 shadow-sm">
        <p className="text-[11px] font-semibold uppercase tracking-[0.18em] text-black/45">
          Prototype pages
        </p>
        <h1 className="mt-2 text-2xl font-semibold">No sections yet</h1>
        <p className="mt-3 text-sm leading-6 text-black/65">
          Add Extension Screenshot HTML files as sections to build your prototype.
        </p>

        <ol className="mt-6 space-y-3 text-sm leading-6 text-black/75">
          <li>
            Save HTML to{' '}
            <code className="rounded bg-[#f7f4f1] px-2 py-1 text-[13px]">
              public/sections/&lt;id&gt;/index.html
            </code>
          </li>
          <li>
            Register the section in{' '}
            <code className="rounded bg-[#f7f4f1] px-2 py-1 text-[13px]">
              src/sections/registry.ts
            </code>
          </li>
        </ol>
      </div>
    </section>
  )
}

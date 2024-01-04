import { onMounted, onUpdated } from 'vue'
import { Streamlit } from '~/stcomponentlib'

export function useStreamlit()
{
	onMounted((): void =>
		{
			Streamlit.setFrameHeight()
		})

	onUpdated((): void =>
		{
			Streamlit.setFrameHeight()
		})
}
